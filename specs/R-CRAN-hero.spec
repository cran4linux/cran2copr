%global packname  hero
%global packver   0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          3%{?dist}%{?buildtag}
Summary:          Spatio-Temporal (Hero) Sandwich Smoother

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-fields 
Requires:         R-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-fields 

%description
An implementation of the sandwich smoother proposed in Fast Bivariate
Penalized Splines by Xiao et al. (2012) <doi:10.1111/rssb.12007>.  A hero
is a specific type of sandwich.  Dictionary.com (2018)
<https://www.dictionary.com> describes a hero as: a large sandwich,
usually consisting of a small loaf of bread or long roll cut in half
lengthwise and containing a variety of ingredients, as meat, cheese,
lettuce, and tomatoes.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
