%global packname  colourvalues
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Assigns Colours to Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 

%description
Maps one of the viridis colour palettes, or a user-specified palette to
values. Viridis colour maps are created by Stéfan van der Walt and
Nathaniel Smith. They were set as the default palette for the 'Python'
'Matplotlib' library, introduced at SciPy 2015 conference
<http://scipy2015.scipy.org/ehome/index.php?eventid=115969&>. Other
palettes available in this library have been derived from 'RColorBrewer'
<https://CRAN.R-project.org/package=RColorBrewer> and 'colorspace'
<https://CRAN.R-project.org/package=colorspace> packages.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
