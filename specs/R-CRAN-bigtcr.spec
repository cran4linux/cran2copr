%global __brp_check_rpaths %{nil}
%global packname  bigtcr
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Analysis of Bivariate Gap Time with CompetingRisks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4

%description
For studying recurrent disease and death with competing risks, comparisons
based on the well-known cumulative incidence function can be confounded by
different prevalence rates of the competing events. Alternatively,
comparisons of the conditional distribution of the survival time given the
failure event type are more relevant for investigating the prognosis of
different patterns of recurrence disease. This package implements a
nonparametric estimator for the conditional cumulative incidence function
and a nonparametric conditional bivariate cumulative incidence function
for the bivariate gap times proposed in Huang et al. (2016)
<doi:10.1111/biom.12494>.

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
