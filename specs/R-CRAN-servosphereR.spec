%global __brp_check_rpaths %{nil}
%global packname  servosphereR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analyze Data Generated from Syntech Servosphere Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3
BuildRequires:    R-CRAN-purrr >= 0.2
Requires:         R-stats >= 3.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-rlang >= 0.3
Requires:         R-CRAN-purrr >= 0.2

%description
Functions that facilitate and speed up the analysis of data produced by a
Syntech servosphere
<http://www.ockenfels-syntech.com/products/locomotion-compensation/>,
which is equipment for studying the movement behavior of arthropods. This
package is designed to make working with data produced from a servosphere
easy for someone new to or unfamiliar with R. The functions provided in
this package fall into three broad-use categories: functions for cleaning
raw data produced by the servosphere software, functions for deriving
movement variables based on position data, and functions for summarizing
movement variables for easier analysis. These functions are built with
functions from the tidyverse package to work efficiently, as a single
servosphere file may consist of hundreds of thousands of rows of data and
a user may wish to analyze hundreds of files at a time. Many of the
movement variables derivable through this package are described in the
following papers: Otálora-Luna, Fernando; Dickens, Joseph C. (2011)
<doi:10.1371/journal.pone.0020990> Party, Virginie; Hanot, Christophe;
Busser, Daniela Schmidt; Rochat, Didier; Renou, Michel (2013)
<doi:10.1371/journal.pone.0052897> Bell, William J.; Kramer, Ernest (1980)
<doi:10.1007/BF01402908> Becher, Paul G; Guerin, Patrick M. (2009)
<doi:10.1016/j.jinsphys.2009.01.006>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
