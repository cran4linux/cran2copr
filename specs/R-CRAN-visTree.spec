%global __brp_check_rpaths %{nil}
%global packname  visTree
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization of Subgroups for Decision Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-partykit 
Requires:         R-rpart 
Requires:         R-CRAN-colorspace 

%description
Provides a visualization for characterizing subgroups defined by a
decision tree structure. The visualization simplifies the ability to
interpret individual pathways to subgroups; each sub-plot describes the
distribution of observations within individual terminal nodes and
percentile ranges for the associated inner nodes.

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
