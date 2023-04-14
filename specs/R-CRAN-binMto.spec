%global __brp_check_rpaths %{nil}
%global packname  binMto
%global packver   0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Many-to-One Comparisons of Proportions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Asymptotic simultaneous confidence intervals for comparison of many
treatments with one control, for the difference of binomial proportions,
allows for Dunnett-like-adjustment, Bonferroni or unadjusted intervals.
Simulation of power of the above interval methods, approximate calculation
of any-pair-power, and sample size iteration based on approximate any-pair
power. Exact conditional maximum test for many-to-one comparisons to a
control.

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
