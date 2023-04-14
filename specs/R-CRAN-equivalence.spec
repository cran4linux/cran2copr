%global __brp_check_rpaths %{nil}
%global packname  equivalence
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          3%{?dist}%{?buildtag}
Summary:          Provides Tests and Graphics for Assessing Tests of Equivalence

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-lattice 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-PairedData 
BuildRequires:    R-grid 
Requires:         R-lattice 
Requires:         R-boot 
Requires:         R-CRAN-PairedData 
Requires:         R-grid 

%description
Provides statistical tests and graphics for assessing tests of
equivalence.  Such tests have similarity as the alternative hypothesis
instead of the null.  Sample data sets are included.

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
