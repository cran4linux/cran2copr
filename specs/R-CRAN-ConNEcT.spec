%global __brp_check_rpaths %{nil}
%global packname  ConNEcT
%global packver   0.7.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.26
Release:          1%{?dist}%{?buildtag}
Summary:          Contingency Measure-Based Networks for Binary Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-Rlab 
Requires:         R-stats 
Requires:         R-graphics 

%description
The ConNEcT approach investigates the pairwise association strength of
binary time series by calculating contingency measures and depicts the
results in a network. The package includes features to explore and
visualize the data. To calculate the pairwise concurrent or temporal
sequenced relationship between the variables, the package provides seven
contingency measures (proportion of agreement, classical & corrected
Jaccard, Cohen's kappa, phi correlation coefficient, odds ratio, and log
odds ratio), however, others can easily be implemented. The package also
includes non-parametric significance tests, that can be applied to test
whether the contingency value quantifying the relationship between the
variables is significantly higher than chance level. Most importantly this
test accounts for auto-dependence and relative frequency.See Bodner et
al.(2021) <doi: 10.1111/bmsp.12222>.Finally, a network can be drawn.
Variables depicted the nodes of the network, with the node size adapted to
the prevalence. The association strength between the variables defines the
undirected (concurrent) or directed (temporal sequenced) links between the
nodes. The results of the non-parametric significance test can be included
by depicting either all links or only the significant ones. Tutorial see
Bodner et al.(2021) <doi: 10.31234/osf.io/2w864>.

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
