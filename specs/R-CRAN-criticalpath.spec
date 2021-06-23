%global __brp_check_rpaths %{nil}
%global packname  criticalpath
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of the Critical Path Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-R6 

%description
An R6 object oriented implementation of the Critical Path Method (CPM).
CPM is a method used to estimate the minimum project duration and
determine the amount of scheduling flexibility on the logical network
paths within the schedule model. The flexibility is in terms of early
start, early finish, late start, late finish, total float and free float.
Beside, it permits to quantify the complexity of network diagram through
the analysis of topological indicators. Finally, it permits to change the
activities duration to perform what-if scenario analysis. The package was
built based on following references: To make topological sorting and other
graph operation, we use Csardi, G. & Nepusz, T. (2005)
<https://www.researchgate.net/publication/221995787_The_Igraph_Software_Package_for_Complex_Network_Research>;
For schedule concept, the reference was Project Management Institute
(2017) <https://www.pmi.org/pmbok-guide-standards/foundational/pmbok>; For
standards terms, we use Project Management Institute (2017)
<https://www.pmi.org/pmbok-guide-standards/lexicon>; For algorithms on
Critical Path Method development, we use Vanhoucke, M. (2013)
<doi:10.1007/978-3-642-40438-2> and Vanhoucke, M. (2014)
<doi:10.1007/978-3-319-04331-9>; And, finally, for topological
definitions, we use Vanhoucke, M. (2009) <doi:10.1007/978-1-4419-1014-1>.

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
