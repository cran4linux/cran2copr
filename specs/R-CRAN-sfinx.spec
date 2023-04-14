%global __brp_check_rpaths %{nil}
%global packname  sfinx
%global packver   1.7.99
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.99
Release:          3%{?dist}%{?buildtag}
Summary:          Straightforward Filtering Index for AP-MS Data Analysis (SFINX)

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch

%description
The straightforward filtering index (SFINX) identifies true positive
protein interactions in a fast, user-friendly, and highly accurate way. It
is not only useful for the filtering of affinity purification - mass
spectrometry (AP-MS) data, but also for similar types of data resulting
from other co-complex interactomics technologies, such as TAP-MS, Virotrap
and BioID. SFINX can also be used via the website interface at
<http://sfinx.ugent.be>.

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
