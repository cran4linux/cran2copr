%global __brp_check_rpaths %{nil}
%global packname  SP2000
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Catalogue of Life Toolkit

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-urltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-urltools 

%description
A programmatic interface to <http://sp2000.org.cn>, re-written based on an
accompanying 'Species 2000' API. Access tables describing catalogue of the
Chinese known species of animals, plants, fungi, micro-organisms, and
more. This package also supports access to catalogue of life global
<http://catalogueoflife.org>, China animal scientific database
<http://zoology.especies.cn> and catalogue of life Taiwan
<https://taibnet.sinica.edu.tw/home_eng.php>. The development of 'SP2000'
package were supported by Biodiversity Survey and Assessment Project of
the Ministry of Ecology and Environment, China <2019HJ2096001006>,Yunnan
University's "Double First Class" Project <C176240405> and Yunnan
University's Research Innovation Fund for Graduate Students <2019227>.

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
