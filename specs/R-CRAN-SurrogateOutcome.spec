%global __brp_check_rpaths %{nil}
%global packname  SurrogateOutcome
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of the Proportion of Treatment Effect Explained bySurrogate Outcome Information

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-survival 
Requires:         R-stats 
Requires:         R-survival 

%description
Provides functions to estimate the proportion of treatment effect on a
censored primary outcome that is explained by the treatment effect on a
censored surrogate outcome/event. All methods are described in detail in
"Assessing the Value of a Censored Surrogate Outcome" by Parast L, Tian L,
and Cai T which is currently in press at Lifetime Data Analysis. The main
functions are (1) R.q.event() which calculates the proportion of the
treatment effect (the difference in restricted mean survival time at time
t) explained by surrogate outcome information observed up to a selected
landmark time, (2) R.t.estimate() which calculates the proportion of the
treatment effect explained by primary outcome information only observed up
to a selected landmark time, and (3) IV.event() which calculates the
incremental value of the surrogate outcome information.

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
%{rlibdir}/%{packname}/INDEX
