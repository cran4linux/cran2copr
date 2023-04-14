%global __brp_check_rpaths %{nil}
%global packname  cdparcoord
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Top Frequency-Based Parallel Coordinates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-freqparcoord 
BuildRequires:    R-CRAN-partools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-freqparcoord 
Requires:         R-CRAN-partools 

%description
Parallel coordinate plotting with resolutions for large data sets and
missing values.

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
