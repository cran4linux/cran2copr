%global packname  viridisLite
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Default Color Maps from 'matplotlib' (Lite Version)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Implementation of the 'viridis' - the default -, 'magma', 'plasma',
'inferno', and 'cividis' color maps for 'R'. 'viridis', 'magma', 'plasma',
and 'inferno' are ported from 'matplotlib' <http://matplotlib.org/>, a
popular plotting library for 'python'. 'cividis', was developed by Jamie
R. Nuñez and Sean M. Colby. These color maps are designed in such a way
that they will analytically be perfectly perceptually-uniform, both in
regular form and also when converted to black-and-white. They are also
designed to be perceived by readers with the most common form of color
blindness (all color maps in this package) and color vision deficiency
('cividis' only). This is the 'lite' version of the more complete
'viridis' package that can be found at
<https://cran.r-project.org/package=viridis>.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
