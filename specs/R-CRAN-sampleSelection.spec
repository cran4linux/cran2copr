%global packname  sampleSelection
%global packver   1.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Sample Selection Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula >= 1.1.1
BuildRequires:    R-CRAN-VGAM >= 1.1.1
BuildRequires:    R-CRAN-systemfit >= 1.0.0
BuildRequires:    R-CRAN-mvtnorm >= 0.9.9994
BuildRequires:    R-CRAN-maxLik >= 0.7.3
BuildRequires:    R-CRAN-miscTools >= 0.6.3
BuildRequires:    R-stats 
Requires:         R-CRAN-Formula >= 1.1.1
Requires:         R-CRAN-VGAM >= 1.1.1
Requires:         R-CRAN-systemfit >= 1.0.0
Requires:         R-CRAN-mvtnorm >= 0.9.9994
Requires:         R-CRAN-maxLik >= 0.7.3
Requires:         R-CRAN-miscTools >= 0.6.3
Requires:         R-stats 

%description
Two-step and maximum likelihood estimation of Heckman-type sample
selection models: standard sample selection models (Tobit-2), endogenous
switching regression models (Tobit-5), sample selection models with binary
dependent outcome variable, interval regression with sample selection
(only ML estimation), and endogenous treatment effects models. These
methods are described in the three vignettes that are included in this
package and in econometric textbooks such as Greene (2011, Econometric
Analysis, 7th edition, Pearson).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
