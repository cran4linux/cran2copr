%global __brp_check_rpaths %{nil}
%global packname  RSarules
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Random Sampling Association Rules from a Transaction Dataset

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.4.1
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-arules >= 1.4.1
Requires:         R-Matrix >= 1.2.6
Requires:         R-methods 
Requires:         R-stats 

%description
Implements the Gibbs sampling algorithm to randomly sample association
rules with one pre-chosen item as the consequent from a transaction
dataset. The Gibbs sampling algorithm was proposed in G. Qian, C.R. Rao,
X. Sun and Y. Wu (2016) <DOI:10.1073/pnas.1604553113>.

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
