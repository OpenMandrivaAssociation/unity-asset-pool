Name:           unity-asset-pool
Version:        0.8.23
Release:        2
License:        CC-BY-SA
Summary:        Pool of assets for Unity (icons)
Url:            https://launchpad.net/unity-asset-pool
Group:          Graphical desktop/Other
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch
Provides:       unity-icon-theme = %{version}

%description
This package provides a pool of assets for Unity, currently all the icons.

%prep
%setup -q

%build

%install
# Install panel/launcher resources
pushd panel
for file in *; do
	install -D -m 0644 $file %{buildroot}%{_datadir}/unity/themes/$file
done
popd
pushd launcher
for file in *; do
	install -D -m 0644 $file %{buildroot}%{_datadir}/unity/themes/$file
done
popd
# Install unity-icon-theme
mkdir -p %{buildroot}%{_datadir}/icons/unity-icon-theme/
cp -a unity-icon-theme/* %{buildroot}%{_datadir}/icons/unity-icon-theme/
# Delete Ubuntu branding icons - will inherit the ones from the icon theme defined for GTK+
for file in "distributor-logo.png"; do
	find %{buildroot}%{_datadir} -name $file -type f -delete -print
done

%files
%doc COPYRIGHT README.txt
%{_datadir}/unity/
%{_datadir}/icons/unity-icon-theme



%changelog
* Fri May 18 2012 Crispin Boylan <crisb@mandriva.org> 0.8.23-1
+ Revision: 799505
- New release

* Tue Jan 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.8.22-1
+ Revision: 768051
- removed dir b/c of duplicate file listings
- imported package unity-asset-pool

