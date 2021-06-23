%global __brp_check_rpaths %{nil}
%global packname  Relectoral
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Electoral Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rmarkdown 

%description
Functions to obtain an important number of electoral indicators described
in the package, which can be divided into two large sections: The first
would be the one containing the indicators of electoral
disproportionality, such as, Rae index, Loosemore–Hanby index, etc. The
second group is intended to study the dimensions of the party system vote,
through the indicators of electoral fragmentation, polarization,
volatility, etc. Moreover, multiple seat allocation simulations can also
be performed based on different allocation systems, such as the D'Hondt
method, Sainte-Laguë, etc. Finally, some of these functions have been
built so that, if the user wishes, the data provided by the Spanish
Ministry of Home Office for different electoral processes held in Spain
can be obtained automatically. All the above will allow the users to carry
out deep studies on the results obtained in any type of electoral process.
The methods are described in: Oñate, Pablo and Ocaña, Francisco A. (1999,
ISBN:9788474762815); Ruiz Rodríguez, Leticia M. and Otero Felipe, Patricia
(2011, ISBN:9788474766226).

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
