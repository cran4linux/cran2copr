%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConsensusOPLS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consensus OPLS for Multi-Block Data Fusion

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 

%description
Merging data from multiple sources is a relevant approach for
comprehensively evaluating complex systems. However, the inherent problems
encountered when analyzing single tables are amplified with the generation
of multi-block datasets, and finding the relationships between data layers
of increasing complexity constitutes a challenging task. For that purpose,
a generic methodology is proposed by combining the strength of established
data analysis strategies, i.e. multi-block approaches and the Orthogonal
Partial Least Squares (OPLS) framework to provide an efficient tool for
the fusion of data obtained from multiple sources. The package enables
quick and efficient implementation of the consensus OPLS model for any
horizontal multi-block data structures (observation-based matching).
Moreover, it offers an interesting range of metrics and graphics to help
to determine the optimal number of components and check the validity of
the model through permutation tests. Interpretation tools include score
and loading plots, Variable Importance in Projection (VIP), functionality
predict for SHAP computing, and performance coefficients such as R2, Q2,
and DQ2 coefficients. J. Boccard and D.N. Rutledge (2013)
<doi:10.1016/j.aca.2013.01.022>.

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
