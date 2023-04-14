%global __brp_check_rpaths %{nil}
%global packname  support.BWS3
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Case 3 Best-Worst Scaling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides basic functions that support an implementation of multi-profile
case (Case 3) best-worst scaling (BWS). Case 3 BWS is a question-based
survey method to elicit people's preferences for attribute levels. Case 3
BWS constructs various combinations of attribute levels (profiles) and
then asks respondents to select the best and worst profiles in each choice
set. A main function creates a dataset for the analysis from the choice
sets and the responses to the questions. For details on Case 3 BWS, refer
to Louviere et al. (2015) <doi:10.1017/CBO9781107337855>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
