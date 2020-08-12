%global packname  TextMiningGUI
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Text Mining GUI Interface

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-syuzhet 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-RColorBrewer 

%description
Graphic interface for text analysis, implement a few methods such as
biplots, correspondence analysis, co-occurrence, clustering, topic models,
correlations and sentiments.

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
