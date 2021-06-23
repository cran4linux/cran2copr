%global __brp_check_rpaths %{nil}
%global packname  childhoodmortality
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculating Childhood Mortality Rates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 

%description
Calculates childhood (neonatal, postneonatal, infant, child, and
under-five) mortality rates using Demographic and Health Survey (DHS)
microdata. The 'childhoodmortality' package was developed in accordance to
the methodology outlined in the "DHS Guide to Statistics" (Rutstein 2006,
<http://dhsprogram.com/pubs/pdf/DHSG1/Guide_to_DHS_Statistics_29Oct2012_DHSG1.pdf>)
Specifically, the package uses a synthetic cohort life table approach,
combining mortality probabilities for age segments with actual cohort
mortality experience into more common age segments. Standard errors for
mortality estimates are computed using the jackknife repeated replication
method outlined in the "Estimates of Sampling Errors" appendix of DHS
Final Reports (DHS 2004,
<http://dhsprogram.com/pubs/pdf/FR175/19AppendixB.pdf>). This methodology
controls for sample design.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
