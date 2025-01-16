%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppsbm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering in Longitudinal Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 

%description
Stochastic block model used for dynamic graphs represented by Poisson
processes. To model recurrent interaction events in continuous time, an
extension of the stochastic block model is proposed where every individual
belongs to a latent group and interactions between two individuals follow
a conditional inhomogeneous Poisson process with intensity driven by the
individuals’ latent groups. The model is shown to be identifiable and its
estimation is based on a semiparametric variational
expectation-maximization algorithm. Two versions of the method are
developed, using either a nonparametric histogram approach (with an
adaptive choice of the partition size) or kernel intensity estimators. The
number of latent groups can be selected by an integrated classification
likelihood criterion. Y. Baraud and L. Birgé (2009).
<doi:10.1007/s00440-007-0126-6>. C. Biernacki, G. Celeux and G. Govaert
(2000). <doi:10.1109/34.865189>. M. Corneli, P. Latouche and F. Rossi
(2016). <doi:10.1016/j.neucom.2016.02.031>. J.-J. Daudin, F. Picard and S.
Robin (2008). <doi:10.1007/s11222-007-9046-7>. A. P. Dempster, N. M. Laird
and D. B. Rubin (1977). <http://www.jstor.org/stable/2984875>. G. Grégoire
(1993). <http://www.jstor.org/stable/4616289>. L. Hubert and P. Arabie
(1985). <doi:10.1007/BF01908075>. M. Jordan, Z. Ghahramani, T. Jaakkola
and L. Saul (1999). <doi:10.1023/A:1007665907178>. C. Matias, T. Rebafka
and F. Villers (2018). <doi:10.1093/biomet/asy016>. C. Matias and S. Robin
(2014). <doi:10.1051/proc/201447004>. H. Ramlau-Hansen (1983).
<doi:10.1214/aos/1176346152>. P. Reynaud-Bouret (2006).
<doi:10.3150/bj/1155735930>.

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
