%global packname  rDppDiversity
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Subset Searching Algorithm Using DPP Greedy MAP

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Given item set, item representation vector, and item ratings, find a
subset with better relevance-diversity trade-off. Also provide machine
learning algorithm to learn item representations maximizing log likelihood
under DPP assumption. References: [1]Laming Chen, Guoxin Zhang, and
Hanning
Zhou(2017)<https://lsrs2017.files.wordpress.com/2017/08/lsrs_2017_lamingchen.pdf>
[2]Laming Chen, Guoxin Zhang, and Hanning
Zhou(2018)<https://papers.nips.cc/paper/2018/file/dbbf603ff0e99629dda5d75b6f75f966-Paper.pdf>
[3]Wilhelm, Mark & Ramanathan, Ajith & Bonomo, Alexander & Jain, Sagar &
Chi, Ed & Gillenwater, Jennifer(2018)<doi:10.1145/3269206.3272018>.

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
