%global __brp_check_rpaths %{nil}
%global packname  speff2trial
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Semiparametric efficient estimation for a two-sample treatmenteffect

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.2
Requires:         R-core >= 2.7.2
BuildArch:        noarch
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-survival 
Requires:         R-CRAN-leaps 
Requires:         R-survival 

%description
The package performs estimation and testing of the treatment effect in a
2-group randomized clinical trial with a quantitative, dichotomous, or
right-censored time-to-event endpoint. The method improves efficiency by
leveraging baseline predictors of the endpoint. The inverse probability
weighting technique of Robins, Rotnitzky, and Zhao (JASA, 1994) is used to
provide unbiased estimation when the endpoint is missing at random.

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
