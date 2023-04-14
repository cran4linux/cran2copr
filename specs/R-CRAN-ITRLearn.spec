%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  ITRLearn
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Learning for Individualized Treatment Regime

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-kernlab 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-kernlab 

%description
Maximin-projection learning (MPL, Shi, et al., 2018) is implemented for
recommending a meaningful and reliable individualized treatment regime for
future groups of patients based on the observed data from different
populations with heterogeneity in individualized decision making.
Q-learning and A-learning are implemented for estimating the groupwise
contrast function that shares the same marginal treatment effects. The
packages contains classical Q-learning and A-learning algorithms for a
single stage study as a byproduct. More functions will be added at later
versions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
