%global __brp_check_rpaths %{nil}
%global packname  qte
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Quantile Treatment Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-BMisc 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-msm 
Requires:         R-CRAN-Hmisc 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-BMisc 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-msm 

%description
Provides several methods for computing the Quantile Treatment Effect (QTE)
and Quantile Treatment Effect on the Treated (QTT). The main cases covered
are (i) Treatment is randomly assigned, (ii) Treatment is as good as
randomly assigned after conditioning on some covariates (also called
conditional independence or selection on observables) using the methods
developed in Firpo (2007) <doi:10.1111/j.1468-0262.2007.00738.x>, (iii)
Identification is based on a Difference in Differences assumption (several
varieties are available in the package e.g. Athey and Imbens (2006)
<doi:10.1111/j.1468-0262.2006.00668.x> Callaway and Li (2019)
<https://ssrn.com/abstract=3013341>, Callaway, Li, and Oka (2018)
<doi:10.1016/j.jeconom.2018.06.008>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
