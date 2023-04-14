%global __brp_check_rpaths %{nil}
%global packname  ipwErrorY
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Inverse Probability Weighted Estimation of Average TreatmentEffect with Misclassified Binary Outcome

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 

%description
An implementation of the correction methods proposed by Shu and Yi (2017)
<doi:10.1177/0962280217743777> for the inverse probability weighted (IPW)
estimation of average treatment effect (ATE) with misclassified binary
outcomes. Logistic regression model is assumed for treatment model for all
implemented correction methods, and is assumed for the outcome model for
the implemented doubly robust correction method. Misclassification
probability given a true value of the outcome is assumed to be the same
for all individuals.

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
