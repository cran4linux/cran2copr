%global __brp_check_rpaths %{nil}
%global packname  peptider
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Evaluation of Diversity in Nucleotide Libraries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-discreteRV >= 1.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-discreteRV >= 1.2
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 

%description
Evaluation of diversity in peptide libraries, including NNN, NNB, NNK/S,
and 20/20 schemes. Custom encoding schemes can also be defined. Metrics
for evaluation include expected coverage, relative efficiency, and the
functional diversity of the library. Peptide-level inclusion probabilities
are computable for both the native and custom encoding schemes.

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
