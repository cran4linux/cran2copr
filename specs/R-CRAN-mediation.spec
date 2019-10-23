%global packname  mediation
%global packver   4.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.0
Release:          1%{?dist}
Summary:          Causal Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-boot 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-boot 

%description
We implement parametric and non parametric mediation analysis. This
package performs the methods and suggestions in Imai, Keele and Yamamoto
(2010) <DOI:10.1214/10-STS321>, Imai, Keele and Tingley (2010)
<DOI:10.1037/a0020761>, Imai, Tingley and Yamamoto (2013)
<DOI:10.1111/j.1467-985X.2012.01032.x>, Imai and Yamamoto (2013)
<DOI:10.1093/pan/mps040> and Yamamoto (2013)
<http://web.mit.edu/teppei/www/research/IVmediate.pdf>. In addition to the
estimation of causal mediation effects, the software also allows
researchers to conduct sensitivity analysis for certain parametric models.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
