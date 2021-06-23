%global __brp_check_rpaths %{nil}
%global packname  TestingSimilarity
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrap Test for the Similarity of Dose Response CurvesConcerning the Maximum Absolute Deviation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-DoseFinding 
BuildRequires:    R-CRAN-alabama 
Requires:         R-lattice 
Requires:         R-CRAN-DoseFinding 
Requires:         R-CRAN-alabama 

%description
Provides a bootstrap test which decides whether two dose response curves
can be assumed as equal concerning their maximum absolute deviation. A
plenty of choices for the model types are available, which can be found in
the 'DoseFinding' package, which is used for the fitting of the models.
See <doi:10.1080/01621459.2017.1281813> for details.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
