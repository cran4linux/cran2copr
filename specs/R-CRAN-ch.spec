%global __brp_check_rpaths %{nil}
%global packname  ch
%global packver   0.1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          About some Small Functions

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-pracma 

%description
The solution to some common problems is proposed, as well as a summary of
some small functions. In particular, it provides a useful function for
some problems in chemistry. For example, monoa(), monob() and mono()
function can be used to calculate The pH of weak acid/base. The ggpng()
function can save the PNG format with transparent background. The
period_table() function will show the periodic table. Also the
show_ruler() function will show the ruler. The show_color() function is
funny and easier to show colors. I also provide the symb() function to
generate multiple symbols at once. The csv2vcf() function provides an easy
method to generate a file. The sym2poly() and sym2coef() function can
extract coefficients from polynomials.

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
