%global packname  PrevMap
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          3%{?dist}
Summary:          Geostatistical Modelling of Spatially Referenced Prevalence Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-pdist 
Requires:         R-Matrix 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-truncnorm 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Provides functions for both likelihood-based and Bayesian analysis of
spatially referenced prevalence data. For a tutorial on the use of the R
package, see Giorgi and Diggle (2017) <doi:10.18637/jss.v078.i08>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
