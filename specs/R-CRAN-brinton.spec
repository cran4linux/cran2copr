%global packname  brinton
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          A Graphical EDA Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-GGally 

%description
An automated graphical exploratory data analysis (EDA) tool that
introduces: a.) wideplot() graphics for exploring the structure of a
dataset through a grid of variables and graphic types. b.) longplot()
graphics, which present the entire catalog of available graphics for
representing a particular variable using a grid of graphic types and
variations on these types. c.) plotup() function, which presents a
particular graphic for a specific variable of a dataset. The plotup()
function also makes it possible to obtain the code used to generate the
graphic, meaning that the user can adjust its properties as needed.

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
