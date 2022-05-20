%global __brp_check_rpaths %{nil}
%global packname  cape
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Combined Analysis of Pleiotropy and Epistasis for Diversity Outbred Mice

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-shape >= 1.4.5
BuildRequires:    R-CRAN-regress >= 1.3.21
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-propagate 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-qtl2 
BuildRequires:    R-CRAN-qtl2convert 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-shape >= 1.4.5
Requires:         R-CRAN-regress >= 1.3.21
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-abind 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-here 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-propagate 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-qtl2 
Requires:         R-CRAN-qtl2convert 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Combined Analysis of Pleiotropy and Epistasis infers predictive networks
between genetic variants and phenotypes. It can be used with standard
two-parent populations as well as multi-parent populations, such as the
Diversity Outbred (DO) mice, Collaborative Cross (CC) mice, or the
multi-parent advanced generation intercross (MAGIC) population of
Arabidopsis thaliana. It uses complementary information of pleiotropic
gene variants across different phenotypes to resolve models of epistatic
interactions between alleles. To do this, cape reparametrizes main effect
and interaction coefficients from pairwise variant regressions into
directed influence parameters. These parameters describe how alleles
influence each other, in terms of suppression and enhancement, as well as
how gene variants influence phenotypes. All of the final interactions are
reported as directed interactions between pairs of parental alleles. For
detailed descriptions of the methods used in this package please see the
following references. Carter, G. W., Hays, M., Sherman, A. & Galitski, T.
(2012) <doi:10.1371/journal.pgen.1003010>. Tyler, A. L., Lu, W., Hendrick,
J. J., Philip, V. M. & Carter, G. W. (2013)
<doi:10.1371/journal.pcbi.1003270>.

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
