%global packname  EDMeasure
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Energy-Based Dependence Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-dHSIC >= 2.0
BuildRequires:    R-CRAN-energy >= 1.7.0
BuildRequires:    R-CRAN-rBayesianOptimization >= 1.1.0
Requires:         R-CRAN-dHSIC >= 2.0
Requires:         R-CRAN-energy >= 1.7.0
Requires:         R-CRAN-rBayesianOptimization >= 1.1.0

%description
Implementations of (1) mutual dependence measures and mutual independence
tests in Jin, Z., and Matteson, D. S. (2017) <arXiv:1709.02532>; (2)
independent component analysis methods based on mutual dependence measures
in Jin, Z., and Matteson, D. S. (2017) <arXiv:1709.02532> and Pfister, N.,
et al. (2018) <doi:10.1111/rssb.12235>; (3) conditional mean dependence
measures and conditional mean independence tests in Shao, X., and Zhang,
J. (2014) <doi:10.1080/01621459.2014.887012>, Park, T., et al. (2015)
<doi:10.1214/15-EJS1047>, and Lee, C. E., and Shao, X. (2017)
<doi:10.1080/01621459.2016.1240083>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
