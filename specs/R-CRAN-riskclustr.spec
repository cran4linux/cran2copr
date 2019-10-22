%global packname  riskclustr
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions to Study Etiologic Heterogeneity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-stringr 
Requires:         R-Matrix 

%description
A collection of functions related to the study of etiologic heterogeneity
both across disease subtypes and across individual disease markers. The
included functions allow one to quantify the extent of etiologic
heterogeneity in the context of a case-control study, and provide p-values
to test for etiologic heterogeneity across individual risk factors. Begg
CB, Zabor EC, Bernstein JL, Bernstein L, Press MF, Seshan VE (2013) <doi:
10.1002/sim.5902>.

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
