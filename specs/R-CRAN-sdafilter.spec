%global __brp_check_rpaths %{nil}
%global packname  sdafilter
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Symmetrized Data Aggregation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-POET 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-POET 
Requires:         R-stats 

%description
We develop a new class of distribution free multiple testing rules for
false discovery rate (FDR) control under general dependence. A key element
in our proposal is a symmetrized data aggregation (SDA) approach to
incorporating the dependence structure via sample splitting, data
screening and information pooling. The proposed SDA filter first
constructs a sequence of ranking statistics that fulfill global symmetry
properties, and then chooses a data driven threshold along the ranking to
control the FDR. For more information, see the website below and the
accompanying paper: Du et al. (2020), "False Discovery Rate Control Under
General Dependence By Symmetrized Data Aggregation", <arXiv:2002.11992>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
