%global packname  localgauss
%global packver   0.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.40
Release:          3%{?dist}
Summary:          Estimating Local Gaussian Parameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-matrixStats 

%description
Computational routines for estimating local Gaussian parameters. Local
Gaussian parameters are useful for characterizing and testing for
non-linear dependence within bivariate data. See e.g. Tjostheim and
Hufthammer, Local Gaussian correlation: A new measure of dependence,
Journal of Econometrics, 2013, Volume 172 (1), pages 33-48
<DOI:10.1016/j.jeconom.2012.08.001>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/Makefile
%doc %{rlibdir}/%{packname}/obfun_dv_dv.f90
%doc %{rlibdir}/%{packname}/obfun_dv_dv.msg
%doc %{rlibdir}/%{packname}/obfun_dv.f90
%doc %{rlibdir}/%{packname}/obfun_dv.msg
%doc %{rlibdir}/%{packname}/tapenadehtml
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
