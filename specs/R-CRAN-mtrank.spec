%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mtrank
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ranking using Probabilistic Models and Treatment Choice Criteria

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.0.2
BuildRequires:    R-CRAN-netmeta >= 3.0.2
BuildRequires:    R-CRAN-PlackettLuce 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-meta >= 8.0.2
Requires:         R-CRAN-netmeta >= 3.0.2
Requires:         R-CRAN-PlackettLuce 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Implementation of a novel frequentist approach to produce clinically
relevant treatment hierarchies in network meta-analysis. The method is
based on treatment choice criteria (TCC) and probabilistic ranking models,
as described by Evrenoglou et al. (2024) <DOI:10.48550/arXiv.2406.10612>.
The TCC are defined using a rule based on the minimal clinically important
difference. Using the defined TCC, the study-level data (i.e., treatment
effects and standard errors) are first transformed into a preference
format, indicating either a treatment preference (e.g., treatment A >
treatment B) or a tie (treatment A = treatment B). The preference data are
then synthesized using a probabilistic ranking model, which estimates the
latent ability parameter of each treatment and produces the final
treatment hierarchy. This parameter represents each treatment’s ability to
outperform all the other competing treatments in the network.
Consequently, larger ability estimates indicate higher positions in the
ranking list.

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
