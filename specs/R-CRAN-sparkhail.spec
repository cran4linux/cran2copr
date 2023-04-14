%global __brp_check_rpaths %{nil}
%global packname  sparkhail
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A 'Sparklyr' Extension for 'Hail'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr >= 1.0.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sparklyr.nested 
BuildRequires:    R-utils 
Requires:         R-CRAN-sparklyr >= 1.0.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sparklyr.nested 
Requires:         R-utils 

%description
'Hail' is an open-source, general-purpose, 'python' based data analysis
tool with additional data types and methods for working with genomic data,
see <https://hail.is/>. 'Hail' is built to scale and has first-class
support for multi-dimensional structured data, like the genomic data in a
genome-wide association study (GWAS). 'Hail' is exposed as a 'python'
library, using primitives for distributed queries and linear algebra
implemented in 'scala', 'spark', and increasingly 'C++'. The 'sparkhail'
is an R extension using 'sparklyr' package. The idea is to help R users to
use 'hail' functionalities with the well-know 'tidyverse' syntax, see
<https://www.tidyverse.org/>.

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
