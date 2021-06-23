%global __brp_check_rpaths %{nil}
%global packname  r2dictionary
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Mini-Dictionary for 'R' and 'Markdown' Writing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 

%description
Despite the predominant use of 'R' for data manipulation and various
robust statistical calculations, in recent years, more people from various
disciplines are beginning to use 'R' for other purposes. A critical
milestone that has enabled large influx of users to the 'R' community is
the development of the 'Tidyverse' family of packages and 'Rmarkdown'.
With the latter, one can write all kinds of documents and produce output
in formats such 'HTML' and 'PDF' very easily. In doing this seemlessly,
further tools are needed for such users to easily and freely write in 'R'
for all kinds of purposes. The 'r2dictionary' introduces a means for users
to directly search for definitions of terms from within the 'R'
environment. The source dictionary is an original work of 'The Online
Plain Text English Dictionary (OPTED)'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
