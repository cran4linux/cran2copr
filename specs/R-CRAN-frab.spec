%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frab
%global packver   0.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          How to Add Two R Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-disordR >= 0.9.8.2
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-disordR >= 0.9.8.2
Requires:         R-methods 

%description
Methods to "add" two R tables; also an alternative interpretation of named
vectors as generalized R tables, so that c(a=1,b=2,c=3) + c(b=3,a=-1) will
return c(b=5,c=3).  Uses 'disordR' discipline (Hankin, 2022,
<doi:10.48550/arXiv.2210.03856>).  Extraction and replacement methods are
provided.  The underlying mathematical structure is the Free Abelian
group, hence the name.  To cite in publications please use Hankin (2023)
<doi:10.48550/arXiv.2307.13184>.

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
