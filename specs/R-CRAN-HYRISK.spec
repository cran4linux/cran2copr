%global packname  HYRISK
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Hybrid Methods for Addressing Uncertainty in RISK Assessments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reliaR 
BuildRequires:    R-CRAN-kerdiest 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-rgenoud 
Requires:         R-datasets 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reliaR 
Requires:         R-CRAN-kerdiest 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-rgenoud 

%description
Methods for addressing uncertainty in risk assessments using hybrid
representations of uncertainty (probability distributions, fuzzy numbers,
intervals, probability distributions with imprecise parameters). The
uncertainty propagation procedure combines random sampling using Monte
Carlo method with fuzzy interval analysis of Baudrit et al. (2007)
<doi:10.1109/TFUZZ.2006.876720>. The sensitivity analysis is based on the
pinching method of Ferson and Tucker (2006)
<doi:10.1016/j.ress.2005.11.052>.

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
%{rlibdir}/%{packname}/INDEX
