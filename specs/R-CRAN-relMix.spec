%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  relMix
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Relationship Inference for DNA Mixtures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Familias >= 2.6.1
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-pedFamilias 
BuildRequires:    R-CRAN-pedtools 
Requires:         R-CRAN-Familias >= 2.6.1
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-pedFamilias 
Requires:         R-CRAN-pedtools 

%description
Analysis of DNA mixtures involving relatives by computation of likelihood
ratios that account for dropout and drop-in, mutations, silent alleles and
population substructure. This is useful in kinship cases, like
non-invasive prenatal paternity testing, where deductions about
individuals' relationships rely on DNA mixtures, and in criminal cases
where the contributors to a mixed DNA stain may be related. Relationships
are represented by pedigrees and can include kinship between more than two
individuals. The main function is relMix() and its graphical user
interface relMixGUI(). The implementation and method is described in Dorum
et al. (2017) <doi:doi.org/10.1007/s00414-016-1526-x>, Hernandis et al.
(2019) <doi:doi.org/10.1016/j.fsigss.2019.09.085> and Kaur et al. (2016)
<doi:doi.org/10.1007/s00414-015-1276-1>.

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
