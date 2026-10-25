%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  paretoinfer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Identification of Approximately Pareto-Optimal Alternatives under Noise

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-seqbench >= 0.1.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-seqbench >= 0.1.0
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-utils 

%description
Sequential identification of epsilon-Pareto-optimal alternatives among a
finite set with noisy, possibly correlated objectives. Simultaneous
anytime-valid confidence sequences for every objective of every
alternative (Waudby-Smith and Ramdas, 2024, <doi:10.1093/jrsssb/qkad009>)
certify, at any time, which alternatives are epsilon-dominated and which
are not, report the estimated frontier, the plausible Pareto set and the
certified-dominated set, propose the next alternative to evaluate, and
record an auditable result contract.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
