%global packname  PerFit
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}
Summary:          Person Fit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-irtoys 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-mirt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-irtoys 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
Several person-fit statistics (PFSs) are offered. These statistics allow
assessing whether individual response patterns to tests or questionnaires
are (im)plausible given the other respondents in the sample or given a
specified item response theory model. Some PFSs apply to dichotomous data,
such as the likelihood-based PFSs (lz, lz*) and the group-based PFSs
(personal biserial correlation, caution index, (normed) number of Guttman
errors, agreement/disagreement/dependability statistics, U3, ZU3, NCI,
Ht). PFSs suitable to polytomous data include extensions of lz, U3, and
(normed) number of Guttman errors.

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
%{rlibdir}/%{packname}/INDEX
