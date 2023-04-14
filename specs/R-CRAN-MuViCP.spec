%global __brp_check_rpaths %{nil}
%global packname  MuViCP
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          MultiClass Visualizable Classification using Combination ofProjections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
Requires:         R-CRAN-sm 
Requires:         R-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 

%description
An ensemble classifier for multiclass classification. This is a novel
classifier that natively works as an ensemble. It projects data on a large
number of matrices, and uses very simple classifiers on each of these
projections. The results are then combined, ideally via Dempster-Shafer
Calculus.

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
