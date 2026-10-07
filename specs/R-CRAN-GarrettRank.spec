%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GarrettRank
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Garrett Ranking Analysis and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-rlang 

%description
Performs Garrett ranking analysis of respondent-ranked items such as
constraints, problems, factors, or priorities. The package converts
respondent rankings into Garrett scores, calculates mean Garrett scores
and final ranks and provides methods for summarizing,tabulating and
visualizing ranking results. It also provides Kendall's coefficient of
concordance for assessing the degree of agreement among respondents.
Garrett ranking does not accommodate tied ranks and Kendall's coefficient
of concordance is likewise computed for untied ranking data.For more
details see Garrett and Woodworth (1969)
<https://books.google.com/books?id=aoqSmQEACAAJ> and Buragohain and Dubey
(2021) <doi:10.5958/2454-552X.2021.00055.4>.

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
