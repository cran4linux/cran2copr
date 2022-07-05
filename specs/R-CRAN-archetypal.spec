%global __brp_check_rpaths %{nil}
%global packname  archetypal
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finds the Archetypal Analysis of a Data Frame

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-inflection 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-entropy 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-inflection 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-lpSolve 
Requires:         R-methods 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-entropy 

%description
Performs archetypal analysis by using Principal Convex Hull Analysis under
a full control of all algorithmic parameters. It contains a set of
functions for determining the initial solution, the optimal algorithmic
parameters and the optimal number of archetypes. Post run tools are also
available for the assessment of the derived solution. Morup, M., Hansen,
LK (2012) <doi:10.1016/j.neucom.2011.06.033>. Hochbaum, DS, Shmoys, DB
(1985) <doi:10.1287/moor.10.2.180>. Eddy, WF (1977)
<doi:10.1145/355759.355768>. Barber, CB, Dobkin, DP, Huhdanpaa, HT (1996)
<doi:10.1145/235815.235821>. Christopoulos, DT (2016)
<doi:10.2139/ssrn.3043076>. Falk, A., Becker, A., Dohmen, T., Enke, B.,
Huffman, D., Sunde, U. (2018), <doi:10.1093/qje/qjy013>. Christopoulos, DT
(2015) <doi:10.1016/j.jastp.2015.03.009> . Murari, A., Peluso, E.,
Cianfrani, Gaudio, F., Lungaroni, M., (2019), <doi:10.3390/e21040394>.

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
