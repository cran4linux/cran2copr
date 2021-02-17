%global packname  EGAnet
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Graph Analysis - A Framework for Estimating the Number of Dimensions in Multivariate Data Using Network Psychometrics

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GGally >= 2.0.0
BuildRequires:    R-CRAN-qgraph >= 1.4.1
BuildRequires:    R-CRAN-NetworkToolbox >= 1.4.0
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-network >= 1.16.0
BuildRequires:    R-CRAN-glasso >= 1.10
BuildRequires:    R-CRAN-semPlot >= 1.0.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-lavaan >= 0.5.22
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-GGally >= 2.0.0
Requires:         R-CRAN-qgraph >= 1.4.1
Requires:         R-CRAN-NetworkToolbox >= 1.4.0
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-network >= 1.16.0
Requires:         R-CRAN-glasso >= 1.10
Requires:         R-CRAN-semPlot >= 1.0.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-lavaan >= 0.5.22
Requires:         R-stats 
Requires:         R-methods 

%description
Implements the Exploratory Graph Analysis (EGA) framework for
dimensionality and psychometric assessment. EGA is part of a new area
called network psychometrics that uses undirected network models for the
assessment of psychometric properties. EGA estimates the number of
dimensions (or factors) using graphical lasso or Triangulated Maximally
Filtered Graph (TMFG) and a weighted network community detection
algorithm. A bootstrap method for verifying the stability of the
dimensions and items in those dimensions is available. The fit of the
structure suggested by EGA can be verified using Entropy Fit Indices. A
novel approach called Unique Variable Analysis (UVA) can be used to
identify and reduce redundant variables in multivariate data. Network
loadings, which are roughly equivalent to factor loadings when the data
generating model is a factor model, are available. Network scores can also
be computed using the network loadings. Dynamic EGA (dynEGA) will estimate
dimensions from time series data for individual, group, and sample levels.
Golino, H., & Epskamp, S. (2017) <doi:10.1371/journal.pone.0174035>.
Golino, H., Shi, D., Christensen, A. P., Garrido, L. E., Nieto, M. D.,
Sadana, R., & Thiyagarajan, J. A. (2020) <doi:10.1037/met0000255>.
Christensen, A. P., & Golino, H. (under review)
<doi:10.31234/osf.io/hz89e>. Golino, H., Moulder, R. G., Shi, D.,
Christensen, A. P., Garrido, L. E., Nieto, M. D., Nesselroade, J., Sadana,
R., Thiyagarajan, J. A., & Boker, S. M. (2020)
<doi:10.31234/osf.io/mtka2>. Christensen, A. P. & Golino, H. (2019)
<doi:10.31234/osf.io/9deay>. Christensen, A. P., Garrido, L. E., & Golino,
H. (under review) <doi:10.31234/osf.io/4kra2>. Golino, H., Christensen, A.
P., Moulder, R. G., Kim, S., & Boker, S. M. (under review)
<doi:10.31234/osf.io/tfs7c>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
