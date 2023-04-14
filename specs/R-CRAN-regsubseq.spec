%global __brp_check_rpaths %{nil}
%global packname  regsubseq
%global packver   0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12
Release:          3%{?dist}%{?buildtag}
Summary:          Detect and Test Regular Sequences and Subsequences

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
For a sequence of event occurence times, we are interested in finding
subsequences in it that are too "regular". We define regular as being
significantly different from a homogeneous Poisson process. The departure
from the Poisson process is measured using a L1 distance. See Di and
Perlman 2007 for more details.

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
