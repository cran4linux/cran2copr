%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UniversalCVI
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hard and Soft Cluster Validity Indices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mclust 

%description
Algorithms for checking the accuracy of a clustering result with known
classes, computing cluster validity indices, and generating plots for
comparing them. The package is compatible with K-means, fuzzy C means, EM
clustering, and hierarchical clustering (single, average, and complete
linkage). The details of the indices in this package can be found in: C.
Alok. (2010) <https://hdl.handle.net/10603/93443>, J. C. Bezdek, M.
Moshtaghi, T. Runkler, C. Leckie (2016) <doi:10.1109/TFUZZ.2016.2540063>,
T. Calinski, J. Harabasz (1974) <doi:10.1080/03610927408827101>, C. H.
Chou, M. C. Su, E. Lai (2004) <doi:10.1007/s10044-004-0218-1>, D. L.
Davies, D. W. Bouldin (1979) <doi:10.1109/TPAMI.1979.4766909>, J. C. Dunn
(1973) <doi:10.1080/01969727308546046>, F. Haouas, Z. Ben Dhiaf, A.
Hammouda, B. Solaiman (2017) <doi:10.1109/FUZZ-IEEE.2017.8015651>, M. Kim,
R. S. Ramakrishna (2005) <doi:10.1016/j.patrec.2005.04.007>, S. H. Kwon
(1998) <doi:10.1049/EL:19981523>, S. H. Kwon, J. Kim, S. H. Son (2021)
<doi:10.1049/ell2.12249>, G. W. Miligan (1980) <doi:10.1007/BF02293907>,
M. K. Pakhira, S. Bandyopadhyay, U. Maulik (2004)
<doi:10.1016/j.patcog.2003.06.005>, M. Popescu, J. C. Bezdek, T. C.
Havens, J. M. Keller (2013) <doi:10.1109/TSMCB.2012.2205679>, S. Saitta,
B. Raphael, I. Smith (2007) <doi:10.1007/978-3-540-73499-4_14>, A.
Starczewski (2017) <doi:10.1007/s10044-015-0525-8>, Y. Tang, F. Sun, Z.
Sun (2005) <doi:10.1109/ACC.2005.1470111>, N. Wiroonsri (2024)
<doi:10.1016/j.patcog.2023.109910>, N. Wiroonsri, O. Preedasawakul (2023)
<arXiv:2308.14785>, C. H. Wu, C. S. Ouyang, L. W. Chen, L. W. Lu (2015)
<doi:10.1109/TFUZZ.2014.2322495> and X. Xie, G. Beni (1991)
<doi:10.1109/34.85677>.

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
