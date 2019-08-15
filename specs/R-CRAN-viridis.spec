%global packname  viridis
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Default Color Maps from 'matplotlib'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-viridisLite >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-viridisLite >= 0.3.0
Requires:         R-stats 
Requires:         R-CRAN-gridExtra 

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
('cividis' only).

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
